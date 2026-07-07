class MeowdokuSolver:
    def __init__(self):
        self.board = None

    def load_board(self, board):
        """
        board 为后续识别得到的棋盘数据
        """
        self.board = board

    def next_hint(self):
        """
        返回下一步提示
        """
        if self.board is None:
            return {
                "success": False,
                "message": "棋盘尚未识别"
            }

        return {
            "success": True,
            "message": "棋盘已读取，推理功能开发中。"
        }
