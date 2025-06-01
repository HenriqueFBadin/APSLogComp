import re


class PrePro:
    @staticmethod
    def filter(code):
        code_sem_comentarios = re.sub(r"//.*", "", code)
        code_sem_tabs = re.sub(r"\t", "", code_sem_comentarios)
        return code_sem_tabs
