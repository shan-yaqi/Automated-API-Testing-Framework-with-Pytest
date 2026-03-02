import logging

# ANSI 颜色码（仅用于控制台）
COLORS = {
    'DEBUG': '\033[36m',  # Cyan
    'INFO': '\033[32m',  # Green
    'WARNING': '\033[33m',  # Yellow (closest to orange)
    'ERROR': '\033[31m',  # Red
    'CRITICAL': '\033[35m',  # Magenta
    'RESET': '\033[0m'  # Reset to default
}

class ColoredFormatter(logging.Formatter):
    def format(self,record):
        log_color = COLORS.get(record.levelname, COLORS['RESET'])
        orig_levelname = record.levelname
        orig_msg = record.msg

        record.levelname = f"{log_color}{record.levelname}{COLORS['RESET']}"
        record.msg = f"{log_color}{record.getMessage()}{COLORS['RESET']}"

        formatted = super().format(record)
        # 恢复原始值
        record.levelname = orig_levelname
        record.msg = orig_msg
        return formatted