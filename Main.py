import random
import time
from tqdm import tqdm

Harmony = """██╗  ██╗ █████╗ ██████╗ ███╗   ███╗ ██████╗ ███╗   ██╗██╗   ██╗
██║  ██║██╔══██╗██╔══██╗████╗ ████║██╔═══██╗████╗  ██║╚██╗ ██╔╝
███████║███████║██████╔╝██╔████╔██║██║   ██║██╔██╗ ██║ ╚████╔╝ 
██╔══██║██╔══██║██╔══██╗██║╚██╔╝██║██║   ██║██║╚██╗██║  ╚██╔╝  
██║  ██║██║  ██║██║  ██║██║ ╚═╝ ██║╚██████╔╝██║ ╚████║   ██║   
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   """

Kernal ="""██╗  ██╗███████╗██████╗ ███╗   ██╗ █████╗ ██╗     
██║ ██╔╝██╔════╝██╔══██╗████╗  ██║██╔══██╗██║     
█████╔╝ █████╗  ██████╔╝██╔██╗ ██║███████║██║     
██╔═██╗ ██╔══╝  ██╔══██╗██║╚██╗██║██╔══██║██║     
██║  ██╗███████╗██║  ██║██║ ╚████║██║  ██║███████╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝"""
Installer="""██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     ███████╗██████╗ 
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     ██╔════╝██╔══██╗
██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     █████╗  ██████╔╝
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     ██╔══╝  ██╔══██╗
██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗███████╗██║  ██║
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
"""

YYLX = """                    ######                            ######              ##                  ##                    ##                  
  ##      ##########                ##      ##########                    ##    ##################          ##      ##                  
    ####    ##    ##    ##            ####    ##    ##    ##            ##  ##          ##                  ##      ##      ##          
      ##      ##  ##  ##                ##      ##  ##  ##              ##    ##      ##      ##            ####################        
            ##    ##                          ##    ##                ##        ##################          ##      ##                  
            ##############                    ##############        ##  ##        ##          ##          ##        ##                  
########  ##      ##              ########  ##      ##                    ##      ##    ##    ##                    ##          ##      
      ##          ##      ##            ##          ##      ##                    ##    ##    ##      ##############################    
      ########################          ########################    ################    ##    ##                ##    ##                
      ##          ##                    ##          ##                          ####    ##    ##                ##    ##                
      ##    ##    ##    ##              ##    ##    ##    ##                  ##  ##    ##    ##                ##    ##                
      ##    ##############              ##    ##############            ##  ##    ##    ##    ##              ##      ##                
      ##    ##          ##              ##    ##          ##              ##          ##  ##                  ##      ##          ##    
    ##  ##                ####        ##  ##                ####            ##        ##    ##              ##        ##          ##    
  ##      ##################        ##      ##################              ##      ##        ####        ##            ############    
                                                                                ####            ##      ##                              
"""

user_agreement_text ="""
请您在安装前仔细阅读本用户协议。Harmony 内核开源软件用户协议：本协议是您与菊
花科技无限领先责任有限公司之间关于Harmony内核开源软件安装和使用的法律协议。
本软件是从鸿蒙系统移植而来的开源项目，遵循开源许可证协议【遥遥领先开源协议】。
您安装或使用本软件，即表示您已阅读、理解并同意遵守本协议的全部内容。本软件按
“现状”提供，菊花科技无限领先责任有限公司不提供任何明示或暗示的担保，不保证
其功能将满足您的要求，也不保证其运行不会中断或没有错误。您应对因安装、使用本
软件而可能导致的任何数据丢失、系统损坏或其他直接或间接的损失自行承担全部风险。 
在任何情况下，菊花科技无限领先责任有限公司均不对您因使用或无法使用本软件而引
起的任何直接、间接、附带、特殊、惩罚性或后果性损害承担责任。如果您不同意本协
议的任何条款，请勿安装或使用本软件。本协议的订立、执行和解释均受中华人民共和
国法律管辖。
"""

speed = 1

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_color(text,color):
    print(f"{color}{text}{Colors.ENDC}")

def print_log(prefix,color):
    min_len,max_len = 5,15
    random_dir = ["program File","root","dev","harmony","huawei","kernal","device","open","bin","lib","etc","opt","proc"]
    text = f"{prefix}"
    for i in range(random.randint(min_len,max_len)):
        text += f"/{random_dir[random.randint(0,len(random_dir)-1)]}"
    print_color(text,color)

def print_process(text,max_stop=0.1):
    print(text)
    for i in tqdm(range(100)): time.sleep(random.random()*max_stop)


def print_logo():
    print_color(Harmony,Colors.OKGREEN)
    print_color(Kernal,Colors.OKGREEN)
    print_color(Installer,Colors.HEADER)

def user_agreement():
    print_color(user_agreement_text,Colors.OKBLUE)
    user_input = input("请仔细阅读上述用户协议，如果统一请按 Y 继续：")
    if user_input == "y" or user_input == "Y": 
        print("\n")
        return
    exit()

def install_kernal():
    for i in range(1000):
        time.sleep(random.random()*0.05 * speed)
        print_log("正在抽取：",Colors.OKBLUE)
    print_color("内核提取完成，即将开始安装",Colors.OKGREEN)
    for i in [
        "正在备份 windows 系统，请勿关闭程序",
        "正在关闭 windows 非核心应用，请勿关闭程序",
        "正在创建 Harmony 分区，请勿关闭程序",
        "正在安装 Harmony 内核镜像，请勿关闭程序",
        "正在安装 Harmony 核心依赖库，请勿关闭程序",
        "正在安装 Harmony Kernal，请勿关闭程序",
        "正在安装 Harmony 核心系统运行环境，请勿关闭程序",
        "正在安装 Harmony 引导，请勿关闭程序",
        "正在安装 Harmony 最小化运行环境，请勿关闭程序",
        "正在安装 Harmony 必要系统软件，请勿关闭程序"
        "正在恢复 windows 系统，请勿关闭程序"
        "正在测试 Harmony 运行是否征程，请勿关闭程序"
    ]:print_process(i,random.random()*0.6 * speed)
    print_color("Harmony Kernal 运行成功！，目前看起来一切非常顺利，接下来将为你安装山海经窗口调度器！",Colors.OKGREEN)
    time.sleep(1)

def install_window():
    for i in range(1000):
        time.sleep(random.random()*0.05 * speed)
        print_log("正在抽取山海经窗口调度器：",Colors.OKBLUE)
    print_color("山海经窗口调度器程序提取完成，即将开始安装",Colors.OKGREEN)
    time.sleep(0.5)
    for i in [
        "正在安装山海经窗口调度器，请勿关闭程序",
        "正在修改窗口显示程序，请勿关闭程序",
        "正在安装窗口自动化聚焦程序，请勿关闭程序",
        "正在遥遥领先，请勿关闭程序",
    ]:print_process(i,random.random()*0.3 *speed)
    print_color(YYLX,Colors.HEADER)
    print_color("海经窗口调度器安装成功，请重启您的计算机，使其能够生效！！",Colors.OKGREEN)


if __name__ == "__main__":
    print("\n\n")
    print_logo()
    user_agreement()
    install_kernal()
    install_window()
