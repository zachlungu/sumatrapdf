{
    'targets': [
        {
            'target_name': 'utils',
            'type': 'static_library',
            'variables':  {
                'src' : '../src/utils',
                'src2' : '../src/wingui',
            },
            'dependencies': [
                'lzma.gyp:lzma',
                'zlib.gyp:zlib',
                'unarr.gyp:unarr',
                'libwebp.gyp:libwebp',
            ],
            'include_dirs': [
                "<(src)",
                "<(src2)",
                "../mupdf/include",
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                    "<(src)",
                    "<(src2)",
                ],
            },
            'msvs_disabled_warnings': [4996],
            'sources': [
                "<(src)/Allocator.h",
                "<(src)/ArchUtil.cpp",
                "<(src)/ArchUtil.h",
                "<(src)/BaseUtil.cpp",
                "<(src)/BaseUtil.h",
                "<(src)/BitManip.h",
                "<(src)/BitReader.cpp",
                "<(src)/BitReader.h",
                "<(src)/ByteOrderDecoder.cpp",
                "<(src)/ByteOrderDecoder.h",
                "<(src)/ByteReader.h",
                "<(src)/ByteWriter.h",
                "<(src)/CmdLineParser.cpp",
                "<(src)/CmdLineParser.h",
                "<(src)/CryptoUtil.cpp",
                "<(src)/CryptoUtil.h",
                "<(src)/CssParser.cpp",
                "<(src)/CssParser.h",
                "<(src)/DbgHelpDyn.cpp",
                "<(src)/DbgHelpDyn.h",
                "<(src)/DebugLog.cpp",
                "<(src)/DebugLog.h",
                "<(src)/Dict.cpp",
                "<(src)/Dict.h",
                "<(src)/DirIter.cpp",
                "<(src)/DirIter.h",
                "<(src)/Dpi.cpp",
                "<(src)/Dpi.h",
                "<(src)/FileTransactions.cpp",
                "<(src)/FileTransactions.h",
                "<(src)/FileUtil.cpp",
                "<(src)/FileUtil.h",
                "<(src)/FileWatcher.cpp",
                "<(src)/FileWatcher.h",
                "<(src)/FrameTimeoutCalculator.h",
                "<(src)/FzImgReader.cpp",
                "<(src)/FzImgReader.h",
                "<(src)/GdiPlusUtil.cpp",
                "<(src)/GdiPlusUtil.h",
                "<(src)/GeomUtil.h",
                "<(src)/HtmlParserLookup.cpp",
                "<(src)/HtmlParserLookup.h",
                "<(src)/HtmlPrettyPrint.cpp",
                "<(src)/HtmlPrettyPrint.h",
                "<(src)/HtmlPullParser.cpp",
                "<(src)/HtmlPullParser.h",
                "<(src)/HtmlWindow.cpp",
                "<(src)/HtmlWindow.h",
                "<(src)/HttpUtil.cpp",
                "<(src)/HttpUtil.h",
                "<(src)/JsonParser.cpp",
                "<(src)/JsonParser.h",
                "<(src)/LzmaSimpleArchive.cpp",
                "<(src)/LzmaSimpleArchive.h",
                "<(src)/NoFreeAllocator.cpp",
                "<(src)/NoFreeAllocator.h",
                "<(src)/PalmDbReader.cpp",
                "<(src)/PalmDbReader.h",
                "<(src)/RefCounted.h",
                "<(src)/Scoped.h",
                "<(src)/SerializeTxt.cpp",
                "<(src)/SerializeTxt.h",
                "<(src)/SettingsUtil.cpp",
                "<(src)/SettingsUtil.h",
                "<(src)/SimpleLog.h",
                "<(src)/SquareTreeParser.cpp",
                "<(src)/SquareTreeParser.h",
                "<(src)/StrFormat.cpp",
                "<(src)/StrFormat.h",
                "<(src)/StrHash.h",
                "<(src)/StrSlice.cpp",
                "<(src)/StrSlice.h",
                "<(src)/StrUtil.cpp",
                "<(src)/StrUtil.h",
                "<(src)/TgaReader.cpp",
                "<(src)/TgaReader.h",
                "<(src)/ThreadUtil.cpp",
                "<(src)/ThreadUtil.h",
                "<(src)/Timer.h",
                "<(src)/Touch.cpp",
                "<(src)/Touch.h",
                "<(src)/TrivialHtmlParser.cpp",
                "<(src)/TrivialHtmlParser.h",
                "<(src)/TxtParser.cpp",
                "<(src)/TxtParser.h",
                "<(src)/UITask.cpp",
                "<(src)/UITask.h",
                "<(src)/UtAssert.cpp",
                "<(src)/UtAssert.h",
                "<(src)/VarintGob.cpp",
                "<(src)/VarintGob.h",
                "<(src)/Vec.h",
                "<(src)/VecSegmented.h",
                "<(src)/WebpReader.cpp",
                "<(src)/WebpReader.h",
                "<(src)/WinUtil.cpp",
                "<(src)/WinUtil.h",
                "<(src)/ZipUtil.cpp",
                "<(src)/ZipUtil.h",
                "<(src)/mingw_compat.h",

                "<(src2)/DialogSizer.cpp",
                "<(src2)/DialogSizer.h",
                "<(src2)/EditCtrl.cpp",
                "<(src2)/EditCtrl.h",
                "<(src2)/FrameRateWnd.cpp",
                "<(src2)/FrameRateWnd.h",
                "<(src2)/LabelWithCloseWnd.cpp",
                "<(src2)/LabelWithCloseWnd.h",
                "<(src2)/SplitterWnd.cpp",
                "<(src2)/SplitterWnd.h",
                "<(src2)/Win32Window.cpp",
                "<(src2)/Win32Window.h",
            ],
        }
    ],
}
