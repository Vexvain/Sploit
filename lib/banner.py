import os
import random

VERSION = "1"


def banner_1(line_sep="#--", space=" " * 30):
    banner = """\033[0m\033[91m{space_sep}
Author : VEXVAIN          
Type   : Mass Exploiter  ███████╗██████╗ ██╗      ██████╗ ██╗████████╗
                         ██╔════╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
                         ███████╗██████╔╝██║     ██║   ██║██║   ██║   
                         ╚════██║██╔═══╝ ██║     ██║   ██║██║   ██║   
                         ███████║██║     ███████╗╚██████╔╝██║   ██║   
                         ╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝                                                            
##############################################\033[0m
    """.format(sep1=line_sep, v_num=VERSION, space_sep=space, spacer=" " * 8)
    return banner


def banner_2():
    banner = r"""
{red}--+{end} {red}Everything is vulnerable...{end} {red}+--{end}
{red}--+{end}                  ____            {red}+--{end} 
{red}--+{end}                 / ___)           {red}+--{end}
{red}--+{end}                 \___ \           {red}+--{end}
{red}--+{end}                 (____/           {red}+--{end}
{red}--+{end}            {red}Sploit{end}            {red}+--{end}
{red}--+{end}                VEXVAIN          {red}+--{end}
{red}--+{end}{minor_space2}             v({red}{vnum}{end}){minor_space}             {red}+--{end}
    """.format(vnum=VERSION, red="\033[91m", red="\033[91m", end="\033[0m",
               minor_space=" " * 1 if len(VERSION) == 3 else "",
               minor_space2=" " * 1 if len(VERSION) == 3 else "")
    return banner

def banner_4():
    banner = r"""
{red}           __.   .     , 	{end}
{red}          (__ ._ | _ *-+-	{end}
{red}          .__)[_)|(_)| | 	{end}
{red}              |          	{end}
{red}          _ ._  _ , _ ._		{end}
{red}         (_ ' ( `  )_  .__)	{end}
{red}       ( (  (    )   `)  ) _)	{end}
{red}      (__ (_   (_ . _) _) ,__)	{end}
{red}          `~~`\ ' . /`~~`		{end}
{red}               ;   ;		{end}
{red}               /   \		{end}
{red} _____________/_ __ \_____________ {end}

{red}--------The Nuclear Option--------{end}
{red}-----+({red}{vnum}{end}{red}){spacer}+-----{end}
{red}-----------VEXVAIN----------{end}	  
{red}__________________________________{end}
    """.format(vnum=VERSION, red="\033[91m", red="\033[91m", end="\033[0m",
               spacer=" " * 9 if len(VERSION) == 3 else " " * 7)
    return banner


def banner_5():
    banner = r"""
                  {red}. '  .{end}
               {red}' .( '.) '{end}
       {white}_{end}     {red}('-.)' (`'.) '{end}
      {white}|0|{end}{red}- -(  #sploit  ){end}
   {grey}.--{end}{white}`+'{end}{grey}--.{end}  {red}.  (' -,).(') .{end}
   {grey}|`-----'|{end}   {red}(' .) - ('. ){end}
   {grey}|       |{end}    {red}. (' `.  ){end}
   {grey}|  {red}.-.{end}  {grey}|{end}       {red}` .  `{end}
   {grey}| {red}(0.0){end}{grey} |{end}
   {grey}| {red}>|=|<{end} {grey}|{end}
   {grey}|  {red}`"`{end}{grey}  |{end}
   {grey}|       |{end}
   {grey}|       |{end}
   {grey}`-.___.-'{end}
   v({red}{version}{end})
    """.format(end="\033[0m", grey="\033[91m", white="\033[37m", version=VERSION, red="\033[91m")
    return banner


def banner_main():
    """
    grab a random banner each run
    """
    banners = [
        banner_5, banner_4,
        banner_3, banner_2, banner_1
    ]
    if os.getenv("Graffiti", False):
        return banner_5()
    elif os.getenv("SploitOG", False):
        return banner_1()
    elif os.getenv("Nuclear", False):
        return banner_4()
    elif os.getenv("SploitaSaurusRex", False):
        return banner_3()
    elif os.getenv("Sploit2", False):
        return banner_2()
    else:
        return random.choice(banners)()
