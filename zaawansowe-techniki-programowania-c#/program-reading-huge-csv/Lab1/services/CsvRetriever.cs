using Lab1.mappers;
using Lab1.models;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Lab1.services
{
    class CsvRetriever : DataRetriever
    {
        Dictionary<string, Profit> profit;
        private Director director;

        public CsvRetriever() {
            director = new Director();
        }
        public void retrieveData(string filepath)
        {
            using (var reader = new StreamReader(filepath))
            {

                reader.ReadLine();
                ProfitBuilder builder = new ProfitBuilder();
                while (!reader.EndOfStream)
                {
                    var line = reader.ReadLine();
                    var values = line.Split(',');

                    Product product = new Product();
                    product.setRegion(values[0]);
                    product.setCountry(values[1]);
                    product.setName(values[2]);
                    product.setProfit(Convert.ToDecimal(values[13].Replace(".", ",")));

                    builder.setProduct(product);
                    director.makePolishProfitGenerator(builder);
                }
                profit = builder.getProfits();
            }
        }

        public Dictionary<string, Profit> getProfit()
        {
            return profit;
        }
    }
}
