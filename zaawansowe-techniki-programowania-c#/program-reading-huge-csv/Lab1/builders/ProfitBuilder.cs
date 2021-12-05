using Lab1.interfaces;
using Lab1.models;
using System.Collections.Generic;

namespace Lab1.mappers
{
    class ProfitBuilder : BaseBuilder, Builder 
    {
        private Dictionary<string, Profit> profits;

        public ProfitBuilder() : base() {
            profits = new Dictionary<string, Profit>();
        }

        public void reset()
        {
            sourceData = null;
        }

        public void addProfit()
        {
            if (sourceData.getCountry().Equals("Poland"))
            {
                if (profits.ContainsKey(sourceData.getName()))
                {
                    Profit profit = profits.GetValueOrDefault(sourceData.getName());
                    profit.setProfit(profit.getProfit() + sourceData.getProfit());
                }
                else
                {
                    profits.Add(sourceData.getName(), toPolishProfit(sourceData));
                }
            }
        }

        public Dictionary<string, Profit> getProfits()
        {
            return profits;
        }

        private Profit toPolishProfit(Product from)
        {
            if (from == null) return null;

            Profit to = new Profit();
            to.setName(from.getName());
            to.setProfit(from.getProfit());

            return to;
        }
    }
}
