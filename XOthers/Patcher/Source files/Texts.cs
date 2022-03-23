using System;
using System.Collections.Generic;

namespace Sanchez.Patcher.Source_files
{
    class Texts
    {
        private static Dictionary<string, string> Text = new Dictionary<string, string>
        {
            {"UNKNOWNERROR",                    "Došlo k neznámé, ale kritické chybě. Chybová zpráva, která může pomoci vyřešit problém: \n{0}"},
            {"MISSINGBINARY",                   "Soubor {0} nebyl nalezen, Restartujte patcher."},
            {"CANNOTSTART",                     "Váš antivirus blokuje hru, deaktivujte ho nebo přidejte hru do Výjimek."},
            {"NONETWORK",                       "Nelze se připojit k serveru, zkontrolujte nastavení sítě a zkuste to znovu."},
            {"CONNECTING",                      "Připojování k serveru..."},
            {"LISTDOWNLOAD",                    "Stahování patchlistu..."},
            {"CHECKFILE",                       "{0} se kontroluje..."},
            {"DOWNLOADFILE",                    "{0} se stahuje... {1}/ {2}"},
            {"COMPLETEPROGRESS",                "Celkový postup: {0}%"},
            {"CURRENTPROGRESS",                 "Aktuální soubor: {0}%  |  {1} kb/s"},
            {"CHECKCOMPLETE",                   "Celý client byl aktualizován."},
            {"DOWNLOADCOMPLETE",                "Všechny požadované soubory jsou staženy."},
            {"DOWNLOADSPEED",                   "{0} kb/s"}
        };

        public static string GetText(string Key, params object[] Arguments)
        {
            foreach (var currentItem in Text)
            {
                if(currentItem.Key == Key)
                {
                    return string.Format(currentItem.Value, Arguments); 
                }
            }

            return null;
        }
    }
}
