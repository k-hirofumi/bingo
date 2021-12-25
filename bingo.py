class Bingo:
    #---------------
    #変数
    #---------------
    #ビンゴ表のサイズ
    Size = 0
    #ビンゴ表のデータを保持する配列(Size × Size の配列)
    BingoData = []
    #ビンゴ表の転地行列
    TransposedBingoData = []
    #あたり文字列の個数
    AtariNumber = []
    #あたり文字列を保持する配列
    AtariData = []
    #ビンゴの各行の状態を保持する配列
    JudgeArray = []

    #----------
    #クラス
    #----------
    ##############################################################
    #クラス概要：ビンゴの各行の状態を保持する
    #保持データ：rowData 行にセットされた文字配列
    #            matchCount あたり文字列と一致したマスの数
    ###############################################################
    class Judge:
        Data = []
        MatchCount = 0
        def __init__(self, data):
            self.Data = data

    #---------------
    #コンストラクタ
    #---------------
    #処理なし
    def __init__(self) -> None:
        pass

    #----------
    #callメソッド
    #----------
    ##############################################################
    #メソッド概要：メイン処理
    #引数　なし
    #戻り値　なし
    ###############################################################
    def __call__(self):

        #---データの取得---#

        #ビンゴ表のサイズを入力(3☓3の場合：3を入力)
        self.Size = int(input())
        #ビンゴのマスデータを取得する
        if(not self.GetBingoData()):
            #取得に失敗した場合は処理を終了
            return

        #あとで削除！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        print(self.BingoData)

        #あたり文字列の個数を取得
        self.AtariNumber = int(input())
        #あたり文字列を取得
        self.GetAtariData()

        #あとで削除！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        print(self.AtariData)
        

        #---あたり判定---#

        #取得したビンゴ表の転置行列を取得(当たり判定を行単位で行うため、予め列データを行データに変換しておく)
        for i in range(len(self.BingoData)):
            tmpRow = []
            for j in range(len(self.BingoData[i])):
                tmpRow.append(self.BingoData[j][i])

            self.TransposedBingoData.append(tmpRow)

        
        #あとで削除！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        print(self.TransposedBingoData)

        #ビンゴ表の各行の状態を初期化
        for i in range(len(self.BingoData)):
            self.JudgeArray.append(self.Judge(self.BingoData[i]))

        #ビンゴ表(転置行列後)の各行の状態を初期化
        for i in range(len(self.TransposedBingoData)):
            self.JudgeArray.append(self.Judge(self.TransposedBingoData[i]))

        #斜めの列を初期化
        #ビンゴ表の左斜め列
        tmpRowLeft = []
        #ビンゴ表の右斜め列
        tmpRowRight = []
        for i in range(self.Size):
            tmpRowLeft.append(self.BingoData[i][i])
            tmpRowRight.append(self.BingoData[i][self.Size - i - 1])

        self.JudgeArray.append(self.Judge(tmpRowLeft))
        self.JudgeArray.append(self.Judge(tmpRowRight))


        #あたり判定
        if(self.JudgeAtari()):
            print('yes')
        else:
            print('no')


    #----------
    #メソッド
    #----------  

    ##############################################################
    #メソッド概要：ビンゴのマスデータを取得する
    #引数　なし
    #戻り値　True(成功) or False(失敗)   
    ###############################################################
    def GetBingoData(self):
        #ビンゴに単語を入力(一行単位で入力してください)
        for i in range(self.Size):
            masu = str(input()).split(' ')
            if len(masu) != self.Size:
                print(self.Size + '行目のデータ数が不正です。処理を終了します。')
                return False
            self.BingoData.append(masu)
        
        return True      

    ##############################################################
    #メソッド概要：あたり文字列を取得する
    #引数　なし
    #戻り値　なし
    ###############################################################
    def GetAtariData(self):
        #あたり文字を入力
        for i in range(self.AtariNumber):
            self.AtariData.append(input())


    ##############################################################
    #メソッド概要：あたり判定を行う
    #引数　なし
    #戻り値　True(ビンゴ列あり) or False(ビンゴ列なし)  
    ###############################################################
    def JudgeAtari(self):
        #あたり文字列の配列でループ
        for atariStr in self.AtariData:
            #初期化したビンゴ表の行でループ
            for row in self.JudgeArray:
                print(atariStr)
                print(row.Data)
                if atariStr in row.Data:
                    row.MatchCount += 1
                    print(row.MatchCount)

                    if row.MatchCount == self.Size:
                        return True

        return False


#---------------
#エントリポイント
#---------------
#インスタンス化
bingo = Bingo()
#メイン処理(callメソッドの呼び出し)
bingo()

input()

