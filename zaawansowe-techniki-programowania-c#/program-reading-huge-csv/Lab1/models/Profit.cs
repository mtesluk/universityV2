using System;
using System.Collections.Generic;
using System.Text;

namespace Lab1.models
{
    class Profit
    {
        private string name;
        private decimal profit;

        public decimal getProfit()
        {
            return profit;
        }

        public void setProfit(decimal val)
        {
            profit = val;
        }

        public string getName()
        {
            return name;
        }

        public void setName(string val)
        {
            name = val;
        }
    }
}
