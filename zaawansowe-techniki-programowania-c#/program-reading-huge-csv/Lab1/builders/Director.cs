using Lab1.builders;
using System;
using System.Collections.Generic;
using System.Text;

namespace Lab1.mappers
{
    class Director
    {
        public void makePolishProfitGenerator(Builder builder)
        {
            builder.addProfit();
            builder.reset();
        }
    }
}
