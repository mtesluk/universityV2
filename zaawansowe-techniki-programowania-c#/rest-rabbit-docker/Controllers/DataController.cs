using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using System;
using System.Collections.Generic;
using System.Linq;
using System;
using System.Text;
using RabbitMQ.Client;
using RabbitMQ.Client.Events;

namespace Rest.Controllers
{
    [ApiController]
    [Route("")]
    public class DataController : ControllerBase
    {
        private readonly ILogger<DataController> _logger;

        public DataController(ILogger<DataController> logger)
        {
            _logger = logger;
        }

        [HttpPost]
        [Route("api/dane")]
        public void Post(Data data)
        {
            Send(data);
        }

        void Send(Data data)
        {
            var factory = new ConnectionFactory() { HostName = "rabbitmq", Port = 5672 };
            factory.UserName = "guest";
            factory.Password = "guest";
            using (var connection = factory.CreateConnection())
            using (var channel = connection.CreateModel())
            {
                channel.QueueDeclare(queue: "hello",
                                     durable: false,
                                     exclusive: false,
                                     autoDelete: false,
                                     arguments: null);

                var body = Encoding.UTF8.GetBytes(data.value);

                channel.BasicPublish(exchange: "",
                                         routingKey: "hello",
                                         basicProperties: null,
                                         body: body);

                _logger.LogInformation("Sent {0}", data.value);
            }
        }

        public class Data
        {
            public String value { set; get; }
        }
    }

    
}
