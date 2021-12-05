using Lab1.models;
using System.Collections.Generic;

namespace Lab1
{
    interface DataRetriever
    {
        void retrieveData(string filepath);
        Dictionary<string, Profit> getProfit();
    }
}
