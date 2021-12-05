using Lab1.interfaces;
using Lab1.models;
using System;
using System.Collections.Generic;
using SautinSoft.Document;

namespace Lab1.services
{
    class PolishProfitGenerator : IGenerator
    {
        Dictionary<string, Profit> data;

        public PolishProfitGenerator(Dictionary<string, Profit> d)
        {
            data = d;
        }
        public void generate(String filepath)
        {
            filepath = filepath + "result.pdf";

            DocumentCore dc = new DocumentCore();
            DocumentBuilder db = new DocumentBuilder(dc);
            director(db);
            dc.Save(filepath, new PdfSaveOptions() { Compliance = PdfCompliance.PDF_A1a });
        }

        private void director(DocumentBuilder db)
        {
            setupHeader(db);
            clear(db);
            setupBody(db);
            writeData(db);
        }

        private void setupHeader(DocumentBuilder db)
        {
            Section section = db.Document.Sections[0];
            section.PageSetup.PaperType = PaperType.A4;

            db.CharacterFormat.FontName = "Verdana";
            db.CharacterFormat.Size = 20;
            db.CharacterFormat.FontColor = Color.Red;
            db.Write("Product Raport for polish sales!");
            db.InsertSpecialCharacter(SpecialCharacterType.LineBreak);
            (section.Blocks[0] as Paragraph).ParagraphFormat.Alignment = HorizontalAlignment.Left;
        }

        private void clear(DocumentBuilder db)
        {
            db.CharacterFormat.ClearFormatting();
        }

        private void writeData(DocumentBuilder db)
        {
            foreach (var product in data)
            {
                db.Write(product.Value.getName() + " " + product.Value.getProfit());
                db.InsertSpecialCharacter(SpecialCharacterType.LineBreak);
            }
        }

        private void setupBody(DocumentBuilder db)
        {
            db.CharacterFormat.Size = 14;
            db.CharacterFormat.FontColor = Color.Black;
            db.CharacterFormat.Bold = false;
        }


    }
}
