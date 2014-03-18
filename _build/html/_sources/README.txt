sphinx-markdown
===============

Sphinx用 MarkdownからreStructuredTextに変換する拡張

[mctenshi/sphinx-markdown-sample](https://github.com/mctenshi/sphinx-markdown-sample)を元に作成


必要なもの
----------

* [Python 3.x](http://www.python.org/download/)
* [Sphinx](http://sphinx-users.jp/gettingstarted/index.html)
* [Pandoc 1.12](http://johnmacfarlane.net/pandoc/installing.html) (pandocコマンドが利用できるようにパスを通しておく)

設定方法
--------

1. extフォルダをconf.pyやMakefileがある場所に設置

2. conf.pyを編集

    ```diff
        - source_suffix = '.rst'
        + source_suffix = '.md'
    ```

3. conf.pyの最後尾に追加

    ```python
        sys.path.append(os.path.abspath('exts'))
        extensions = ['sphinxcontrib_markdown']
    ```

4. index.rstのファイル名をindex.mdに変更


ファイル編集
------------

* ファイルの拡張子は.md
* index.mdは拡張子はMarkdownだが、中身はreStructuredTextで書く。（Sphinxのディレクティブなどが使用可能）
* Markdownの構文は[GitHub Flavored Markdown](https://help.github.com/articles/github-flavored-markdown)が利用可能
* その他追加の構文は[Pandoc’s markdown](http://johnmacfarlane.net/pandoc/README.html#pandocs-markdown)を参照。
  拡張機能はext/sphinxcontrib_markdown.pyの19行目のコマンドに追加していく。

