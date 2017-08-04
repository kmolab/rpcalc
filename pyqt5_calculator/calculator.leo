<?xml version="1.0" encoding="utf-8"?>
<!-- Created by Leo: http://leoeditor.com/leo_toc.html -->
<leo_file xmlns:leo="http://leoeditor.com/namespaces/leo-python-editor/1.1" >
<leo_header file_format="2" tnodes="0" max_tnode_index="0" clone_windows="0"/>
<globals body_outline_ratio="0.5" body_secondary_ratio="0.5">
	<global_window_position top="50" left="50" height="500" width="700"/>
	<global_log_window_position top="0" left="0" height="0" width="0"/>
</globals>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="leo.20170729134939.1"><vh>@settings</vh>
<v t="leo.20170729134939.2"><vh>@data qt-gui-plugin-style-sheet</vh></v>
<v t="leo.20170729134939.3"><vh>@string initial_split_orientation = horizontal</vh></v>
</v>
<v t="leo.20170729134935.2" a="E"><vh>use Eric6 to develop PyQt5 program </vh>
<v t="leo.20170729135207.1"><vh>processes</vh></v>
</v>
<v t="leo.20170730003946.1"><vh>Calculator Example</vh></v>
</vnodes>
<tnodes>
<t tx="leo.20170729134935.2"></t>
<t tx="leo.20170729134939.1"></t>
<t tx="leo.20170729134939.2">QTreeWidget {
    /* These apply to the selected item, but not to editing items.*/
    background-color: #ffffec; /* Leo's traditional tree color */
    selection-color: black; /* was white */
    selection-background-color: lightgrey;
    /* font-family: SansSerif; */
    /*font-family: DejaVu Sans Mono;*/
    font-family:YaHei Mono;
    /* 標題字型大小設定 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal, italic,oblique */
 }

/* Headline edit widgets */
QTreeWidget QLineEdit {
    background-color: cornsilk;
    selection-color: white;
    selection-background-color: blue;
    /*font-family: DejaVu Sans Mono;*/    
    font-family:YaHei Mono;
    /* 沒有特別對應字型大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal, italic,oblique */
}

/* The log panes */
QTextEdit {
    background-color: #f2fdff;
    selection-color: red;
    selection-background-color: blue;
    /* font-family: Courier New; */
    font-family:YaHei Mono;
    /* log font 大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal, italic,oblique */
}

/* The body pane */
QTextEdit#richTextEdit {
    background-color: #fdf5f5; /* A kind of pink. */
    selection-color: white;
    selection-background-color: red;
    /*font-family: DejaVu Sans Mono;*/
    /* font-family: Courier New; */
    font-family:YaHei Mono;
    /* 內文字型大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal,italic,oblique */
}

QLabel {
    font-family:YaHei Mono;'CherryPy', 'pytz', 'mako', 'beautifulsoup4', 'pymysql', 'peewee'
    /* 下方的 Minibuffer 標題字型大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal,italic,oblique */
}

/* Editor labels */
QLineEdit#editorLabel {
    background-color: #ffffec;
    font-family:YaHei Mono;
    /* 沒有直接對應字型大小 */
    font-size: 20px;
    font-weight: normal; /* normal,bold,100,..,900 */
    font-style: normal; /* normal,italic,oblique */
    border: 2px;
    margin: 2px;
}</t>
<t tx="leo.20170729134939.3">horizontal: body pane to the left
vertical: body pane on the botton</t>
<t tx="leo.20170729135207.1">Workflow

各 .py 功能物件使用目錄儲存
由介面程式導入其他所有功能物件
然後再由 run.py 導入後顯示待命

1) 利用 Qt Designer 設計介面
2) 編譯成 .py 同時建立對應程式碼
3) 各按鈕分別透過 single-slot 建立處理的對應函式

Eric6 side

Qt Designer side



</t>
<t tx="leo.20170730003946.1">先乘除後加減

1+2*3 -&gt; 1+(2*3)

利用 http://doc.qt.io/qt-5/qtwidgets-widgets-calculator-example.html 與 https://github.com/baoboa/pyqt5/blob/master/examples/widgets/calculator.py 中的資料, 以 Eric 6 IDE 建立一個視窗 calculator.</t>
</tnodes>
</leo_file>
