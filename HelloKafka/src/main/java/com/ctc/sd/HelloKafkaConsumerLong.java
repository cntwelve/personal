package com.ctc.sd;


import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.Producer;
import org.apache.kafka.clients.producer.ProducerRecord;

import java.util.Arrays;
import java.util.Properties;

public class HelloKafkaConsumerLong {
    public static void main(String[] args) {
        boolean deal = true;
        String msg;
        String[] ms;

        // 设置Consumer
        Properties props = new Properties();
        props.put("zookeeper.connect", "192.168.25.100:2181,192.168.25.101:2181,192.168.25.102:2181");
        props.put("bootstrap.servers", "192.168.25.100:6667");
        props.put("group.id", "GroupA");
        props.put("enable.auto.commit", "true");
        props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        props.put("value.deserializer", "org.apache.kafka.common.serialization.LongDeserializer");

        KafkaConsumer<String, String> consumer = new KafkaConsumer<String, String>(props);
        //订阅主题列表topic
        consumer.subscribe(Arrays.asList("testm"));

        ConsumerRecords<String, String> records = null;
        while (true) {
            deal = true;
            records = consumer.poll(100);
            for (ConsumerRecord<String, String> record : records) {
                //　正常这里应该使用线程池处理，不应该在这里处理
                System.out.printf("offset = %d, key = %s, value = %s, timestamp = %s", record.offset(), record.key(), record.value(), record.timestamp() + "\n");

                if (record.key().toLowerCase().contains("a")) {
                    deal = false;
                }
            }
            if (deal == false) {
                break;
            }
        }
        consumer.close();
        System.out.println("Char 'A' received, exit!");
    }

}
