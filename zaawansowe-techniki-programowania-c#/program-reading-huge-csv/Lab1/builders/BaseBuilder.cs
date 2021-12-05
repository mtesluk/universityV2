using Lab1.interfaces;
using Lab1.models;
using System;
using System.Collections.Generic;
using System.Text;

namespace Lab1.mappers
{
    class BaseBuilder
    {
        protected Product sourceData;

        public BaseBuilder()
        {
        }

        public void setProduct(Product value)
        {
            sourceData = value;
        }
    }
}
