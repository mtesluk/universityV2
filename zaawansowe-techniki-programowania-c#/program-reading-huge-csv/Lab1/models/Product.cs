

namespace Lab1.models
{
    class Product
    {
        private string region;
        private string country;
        private string name;
        private decimal profit;

        public override string ToString()
        {
            return region + " " + profit;
        }

        public string getCountry()
        {
            return country;
        }

        public void setCountry(string val)
        {
            country = val;
        }

        public string getName()
        {
            return name;
        }

        public void setName(string val)
        {
            name = val;
        }

        public string getRegion()
        {
            return region;
        }

        public void setRegion(string val)
        {
            region = val;
        }

        public decimal getProfit()
        {
            return profit;
        }

        public void setProfit(decimal val)
        {
            profit = val;
        }
    }
}
