using Lab1.interfaces;
using Lab1.models;
using System;
using System.Collections.Generic;

namespace Lab1.builders
{
    class NameAlphabeticSort : SortStrategy
    {
        public void sort(List<Profit> data)
        {
            data.Sort((u1, u2) => u1.getName().CompareTo(u2.getName()));
        }
    }
}
