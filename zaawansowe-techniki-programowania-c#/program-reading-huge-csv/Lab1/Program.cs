using System.Collections.Generic;
using Lab1.services;
using Lab1.models;
using Lab1.interfaces;

namespace Lab1
{
    class Program
    {
        private IDataService productService;
        private string filenameDataRet = @"C:\Users\mtesluk\Desktop\studia\ZTP\records.csv";
        private string filenameDataSave = @"C:\Users\mtesluk\Desktop\studia\ZTP\";

        static void Main(string[] args)
        {
            // 1 PDF tabela z miesiacem i kontynentem i iloscia zysku kazdego produktu wszystkiego
            // 2 PDF czesc produktow gdzie jest sprzedawana i zysk
            // 3 PDF w Polsce produkty sprzedaz zyski

            var program = new Program();
            program.productService = ProductService.getInstance();

            program.run();
        }

        private void run()
        {

            productService.retrieveData(filenameDataRet);
            productService.generate(filenameDataSave, GenerateType.POLISH_PROFIT);

            /*generator.generatePolishRaport(products, filenameDataSave + "result.pdf");*/
        }
    }
}
