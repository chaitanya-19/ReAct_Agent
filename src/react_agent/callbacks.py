import logging
from datetime import datetime
from pathlib import Path

# Always writes next to callbacks.py regardless of where adk web is run from
LOG_FILE = Path(__file__).parent / "agent_trace.log"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if not logger.handlers:
    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(LOG_FILE)

    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)


def before_model_callback(callback_context, llm_request):
    logger.info("=" * 60)
    logger.info(">>> LLM REQUEST")
    logger.info(f"Timestamp  : {datetime.now().isoformat()}")
    logger.info(f"Model      : {llm_request.model}")

    for i, content in enumerate(llm_request.contents):
        role = content.role
        text = " ".join(p.text for p in content.parts if hasattr(p, "text") and p.text)
        logger.info(f"Message[{i}] : [{role}] {text}")

    return None


def after_model_callback(callback_context, llm_response):
    logger.info("<<< LLM RESPONSE")
    logger.info(f"Model Ver  : {llm_response.model_version}")
    logger.info(f"Finish     : {llm_response.finish_reason}")

    if llm_response.content:
        text = " ".join(
            p.text for p in llm_response.content.parts
            if hasattr(p, "text") and p.text
        )
        logger.info(f"Response   : {text}")

    gm = llm_response.grounding_metadata
    if gm and gm.web_search_queries:
        logger.info(f"Searches   : {gm.web_search_queries}")

    um = llm_response.usage_metadata
    if um:
        logger.info(f"Tokens     : prompt={um.prompt_token_count} | "
                    f"response={um.candidates_token_count} | "
                    f"total={um.total_token_count}")

    logger.info("=" * 60)
    return None