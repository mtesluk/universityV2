using Lab1.interfaces;
using Lab1.mappers;
using Lab1.models;
using System;
using System.Collections.Generic;

namespace Lab1.services
{

    class ProductService : IDataService
    {
        private static ProductService instance;
        private DataRetriever dataRetriever;


        private ProductService()
        {
            dataRetriever = new CsvRetriever();
        }

        public static ProductService getInstance()
        {
            if (instance == null)
            {
                instance = new ProductService();
            }
            return instance;
        }

        public void retrieveData(String filenameDataRet)
        {
            dataRetriever.retrieveData(filenameDataRet);
        }

        public void generate(String filepath, GenerateType type)
        {
            IGenerator generator = null;
            if (type.Equals(GenerateType.POLISH_PROFIT)) {
                generator = new PolishProfitGenerator(dataRetriever.getProfit());
            }
            if (generator != null)
            {
                generator.generate(filepath);
            }
        }
    }
}
