using Lab1.models;
using System;
using System.Collections.Generic;
using System.Text;

namespace Lab1.interfaces
{
    interface IDataService
    {
        public void retrieveData(String filenameDataRet);
        public void generate(String filepathDestiantion, GenerateType strategy);
    }
}
