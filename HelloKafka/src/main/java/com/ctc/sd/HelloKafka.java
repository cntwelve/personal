package com.ctc.sd;


import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.Producer;
import org.apache.kafka.clients.producer.ProducerRecord;

import java.util.Properties;
import java.util.Random;

public class HelloKafka {
    public static void main(String[] args) {
        Properties properties = new Properties();
        properties.put("zookeeper.connect", "192.168.25.100:2181,192.168.25.101:2181,192.168.25.102:2181");
        properties.put("serializer.class", "kafka.serializer.StringEncoder");
        properties.put("bootstrap.servers", "192.168.25.100:6667");
        properties.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        properties.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

        Producer<String, String> producer = new KafkaProducer<String, String>(properties);
        while (true) {
            Random rand = new Random();
            char c = (char) (rand.nextInt(26) + 65);
            System.out.println(c);
            producer.send(new ProducerRecord<String, String>("testn", "Message from test program: " + c + "."));
            if (c == 'A') {
                break;
            }
        }
        producer.close();
    }
}
