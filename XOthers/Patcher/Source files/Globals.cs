using System.Collections.Generic;

namespace Sanchez.Patcher.Source_files
{
    class Globals
    {
        public static string ServerURL = "https://lorderon.eu/files/patcher/";
        public static string PatchlistName  = "patch.list";
        public static string BinaryName     = "client.exe";
        public static string config = "config.exe";

        public static pForm pForm;

        public static List<File>    Files    = new List<File>();
        public static List<string>  OldFiles = new List<string>();

        public static long fullSize;
        public static long completeSize;

        public struct File
        {
            public string Name;
            public string Hash;
            public long   Size;
        }
    }
}
