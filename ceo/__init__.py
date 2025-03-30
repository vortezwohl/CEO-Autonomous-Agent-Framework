import logging

# noinspection PyUnresolvedReferences
from .util.mcp_session import StdioMcpConfig
from .brain.lm import (
    get_openai_model,
    get_dashscope_model,
    get_deepseek_model
)
from .brain.agent import Agent
from .brain.mcp_agent import McpAgent
from .ability import Ability, McpAbility, AgenticAbility
from .util.agentic import agentic
from .util.ability import ability
from .util.synchronized_call import synchronized_call, sync_call
from .util.mcp_session import mcp_session
from .enum import Personality

__AUTHOR__ = '吴子豪 / Vortez Wohl'
__EMAIL__ = 'vortez.wohl@gmail.com'
__VERSION__ = '0.13.0-preview'
__GITHUB__ = 'https://github.com/vortezwohl'
__BLOG__ = 'https://vortezwohl.github.io'

logger = logging.getLogger('ceo')
logger.setLevel(logging.ERROR)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(levelname)s] %(asctime)s %(name)s : %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

logger = logging.getLogger('ceo.prompt')
logger.setLevel(logging.ERROR)
logger = logging.getLogger('ceo.ability')
logger.setLevel(logging.ERROR)
logger = logging.getLogger('ceo.agent')
logger.setLevel(logging.ERROR)
