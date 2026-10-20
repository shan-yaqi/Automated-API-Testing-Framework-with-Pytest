import os
import sys
import subprocess

# 让 `python run\run.py` 这种直接执行方式也能正确解析项目根目录下的包
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from utils.util import RequestUtil

# =========================
# 基础路径配置
# =========================
# abspath dir(常量大写表示“全局配置”)

RESULTS_DIR = os.path.join(os.path.join(RequestUtil.BASE_DIR,"results"),"results_data")
REPORTS_DIR = os.path.join(os.path.join(RequestUtil.BASE_DIR, "results"),"reports_data")
test_dir = os.path.join(RequestUtil.BASE_DIR,"tests")


# If the required folder directories exist, and create them if they do not
os.makedirs(RESULTS_DIR,exist_ok=True)
os.makedirs(REPORTS_DIR,exist_ok=True)

# =========================
# 工具函数
# =========================
# def get_timestamp():
#     """
#     Generate a timestamp
#     """
#     return datetime.now().strftime("%Y%m%d_%H_%M_%S")
# TIMESTAMP = get_timestamp()

def get_dirs_path(logger = None):
    """
    Define directories.
    :return:The absolute paths of the results and report dir
    """
    result_dir = os.path.join(RESULTS_DIR, f"result{RequestUtil.TIMESTAMP}")
    report_dir = os.path.join(REPORTS_DIR, f"report{RequestUtil.TIMESTAMP}")
    try:
        os.makedirs(result_dir,exist_ok=True)
        os.makedirs(report_dir,exist_ok=True)
    except Exception as e:
        logger.error(f"创建目录失败：{e}")
        raise
    return result_dir,report_dir

def run_pytest(result_dir,logger = None):
    """
    Run pytest and generate Allure test datas.
    :return: pytest 退出码 (0=全部通过, 非0=有失败或错误)
    """
    logger.info(f"开始运行pytest，结果目录：{result_dir}")
    try:
        ret = subprocess.run(["pytest","-v",f"{test_dir}",f"--alluredir={result_dir}"])
        if ret.returncode != 0:
            logger.warning(f"pytest执行返回码为{ret.returncode},部分测试可能失败")
        return ret.returncode
    except Exception as e:
        logger.error(f"运行pytest出错：{e}")
        raise

def get_allure_report(result_dir,report_dir,logger=None,open_report=True):
    """
    Generate the Allure report and verify whether it has been opened.
    param open_report: ON or OFF
    """
    # cmd = f"allure generate {result_dir} -o {report_dir} --clean"
    # subprocess.run(cmd, shell=True, check=True)
    logger.info(f"开始生成allure报告，报告目录：{report_dir}")
    try:
        # ret = os.system(f"allure generate {result_dir} -o {report_dir} --clean")
        ret = subprocess.run(
            [
                "allure.bat",
                "generate",
                result_dir,
                "-o",
                report_dir,
                "--clean"
            ]
        )
        if ret.returncode != 0:
            logger.error(f"生成报告失败，返回码：{ret}")
            return
        if open_report:
            # 使用 Popen 非阻塞启动，避免 `allure open` 阻塞主进程
            try:
                subprocess.Popen(["allure.bat", "open", report_dir])
                logger.info(f"成功生成并打开allure报告（后台）！")
            except Exception as e:
                logger.warning(f"打开报告失败：{e}")
        else:
            logger.info(f"成功生成allure报告！")
    except Exception as e:
        logger.error(f"未找到allure命令，请检查Allure是否安装以及PATH配置：{e}")


def main():
    logger = RequestUtil.get_logger(RequestUtil.LOG_DIR,RequestUtil.TIMESTAMP,name="auto_test_logger")
    exit_code = 0
    try:
        result_dir,report_dir = get_dirs_path(logger)
        exit_code = run_pytest(result_dir,logger)

        get_allure_report(result_dir,report_dir,logger,open_report=True)
        logger.info(f"本次测试完成，报告目录：{report_dir}")
    except Exception as e:
        logger.critical(f"程序异常终止：{e}")
        exit_code = 1
    sys.exit(exit_code)

if __name__ == "__main__":
    main()







