from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    logger.error("OPENAI_API_KEY not found in environment variables")
    raise ValueError("OPENAI_API_KEY not found")
client = OpenAI(api_key=api_key)

def generate_answer(question: str) -> str:
    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            tools=[{"type": "web_search_preview"}],
            input=question,
        )
        logger.info(f"Generated answer for question: {question[:50]}...")
        return response.output_text
    except Exception as e:
        logger.error(f"Error generating answer: {str(e)}")
        raise

def convert_currency(amount: float, from_currency: str, to_currency: str) -> dict:
    """Mock currency conversion function (replace with real API in production)."""
    # Mock exchange rates (as of July 2025, for demonstration)
    exchange_rates = {
        "USD": {"EUR": 0.95, "GBP": 0.80, "AUD": 1.55, "CAD": 1.40},
        "EUR": {"USD": 1.05, "GBP": 0.85, "AUD": 1.63, "CAD": 1.47},
        "GBP": {"USD": 1.25, "EUR": 1.18, "AUD": 1.92, "CAD": 1.73},
        "AUD": {"USD": 0.65, "EUR": 0.61, "GBP": 0.52, "CAD": 0.90},
        "CAD": {"USD": 0.71, "EUR": 0.68, "GBP": 0.58, "AUD": 1.11}
    }
    try:
        if from_currency not in exchange_rates or to_currency not in exchange_rates[from_currency]:
            raise ValueError(f"Unsupported currency pair: {from_currency} to {to_currency}")
        converted_amount = amount * exchange_rates[from_currency][to_currency]
        return {
            "amount": round(converted_amount, 2),
            "from_currency": from_currency,
            "to_currency": to_currency
        }
    except Exception as e:
        logger.error(f"Error in currency conversion: {str(e)}")
        raise

def currency_assistant(user_message: str, conversation_history: list = None) -> tuple[str, list]:
    """A complete assistant that handles currency conversion queries."""
    if conversation_history is None:
        conversation_history = []

    # Add the user's new message to the conversation
    conversation_history.append({"role": "user", "content": user_message})

    # Define available tools (currency conversion function)
    tools = [{
        "type": "function",
        "name": "convert_currency",
        "description": "Convert an amount from one currency to another using current exchange rates",
        "parameters": {
            "type": "object",
            "properties": {
                "amount": {
                    "type": "number",
                    "description": "The amount of money to convert"
                },
                "from_currency": {
                    "type": "string",
                    "description": "The currency code to convert from (e.g., USD, EUR, GBP)"
                },
                "to_currency": {
                    "type": "string",
                    "description": "The currency code to convert to (e.g., USD, EUR, GBP)"
                }
            },
            "required": ["amount", "from_currency", "to_currency"],
            "additionalProperties": False
        },
        "strict": True
    }]

    # Get initial response from the model
    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            input=conversation_history,
            tools=tools,
        )
    except Exception as e:
        logger.error(f"Error in initial OpenAI API call: {str(e)}")
        raise

    # Check if the model wants to call a function
    if response.output and isinstance(response.output, list) and response.output[0].type == "function_call":
        tool_call = response.output[0]

        # Process the function call
        try:
            args = json.loads(tool_call.arguments)
            result = convert_currency(**args)
        except Exception as e:
            logger.error(f"Error processing tool call: {str(e)}")
            raise

        # Add the function call and its result to the conversation
        conversation_history.append({"type": "function_call", "name": tool_call.name, "arguments": tool_call.arguments, "call_id": tool_call.call_id})
        conversation_history.append({
            "type": "function_call_output",
            "call_id": tool_call.call_id,
            "output": json.dumps(result)
        })

        # Get the final response with the function results incorporated
        try:
            final_response = client.responses.create(
                model="gpt-4o-mini",
                input=conversation_history,
                tools=tools,
            )
            logger.info(f"Generated currency answer for question: {user_message[:50]}...")
            return final_response.output_text, conversation_history
        except Exception as e:
            logger.error(f"Error in final OpenAI API call: {str(e)}")
            raise
    else:
        logger.info(f"Generated direct answer for question: {user_message[:50]}...")
        return response.output_text, conversation_history

def extract_product_info(description: str) -> dict:
    """Extract structured product information from a description using OpenAI API."""
    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            input=f"Extract structured product information from this description: {description}",
            text={
                "format": {
                    "type": "json_schema",
                    "name": "product_details",
                    "schema": {
                        "type": "object",
                        "properties": {
                            "product_name": {"type": "string"},
                            "category": {"type": "string"},
                            "features": {"type": "array", "items": {"type": "string"}},
                            "colors": {"type": "array", "items": {"type": "string"}},
                            "pricing": {
                                "type": "object",
                                "properties": {
                                    "regular_price": {"type": "number"},
                                    "sale_price": {"type": "number"},
                                    "currency": {"type": "string"},
                                },
                                "additionalProperties": False,
                                "required": ["regular_price", "sale_price", "currency"],
                            },
                        },
                        "required": ["product_name", "features", "colors", "pricing", "category"],
                        "additionalProperties": False,
                    },
                    "strict": True,
                }
            },
        )
        logger.info(f"Extracted product info from description: {description[:50]}...")
        return json.loads(response.output_text)
    except Exception as e:
        logger.error(f"Error extracting product info: {str(e)}")
        raise