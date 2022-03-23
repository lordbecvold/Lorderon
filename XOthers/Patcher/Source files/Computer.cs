﻿using System;
using System.Diagnostics;

namespace Sanchez.Patcher.Source_files
{
    class Computer
    {
        public static long Compute(long Size)
        {
            return (Size * 100 / Globals.fullSize);
        }

        public static double ComputeDownloadSize(double Size)
        {
            return (Size / 1024d / 1024d);
        }

        public static double ComputeDownloadSpeed(double Size, Stopwatch stopWatch)
        {
            return (Size / 1024d / stopWatch.Elapsed.TotalSeconds);
        }
    }
}
