package com.ctc.sd;


import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.Producer;
import org.apache.kafka.clients.producer.ProducerRecord;

import java.util.Arrays;
import java.util.Properties;

public class HelloKafkaConsumer {
    public static void main(String[] args) {
        boolean deal = true;

        Properties props = new Properties();
        props.put("zookeeper.connect", "192.168.25.100:2181,192.168.25.101:2181,192.168.25.102:2181");

        props.put("bootstrap.servers", "192.168.25.100:6667");
//        System.out.println("this is the group part test 1");
//        消费者的组id
        props.put("group.id", "GroupA");
        props.put("enable.auto.commit", "true");
//        props.put("auto.commit.interval.ms", "1000");

        //从poll(拉)的回话处理时长
//        props.put("session.timeout.ms", "30000");
        //poll的数量限制
//props.put("max.poll.records", "100");

        props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");

        KafkaConsumer<String, String> consumer = new KafkaConsumer<String, String>(props);
        //订阅主题列表topic
        consumer.subscribe(Arrays.asList("testn"));

        ConsumerRecords<String, String> records = null;
        while (true) {
            deal = true;
            records = consumer.poll(100);
            for (ConsumerRecord<String, String> record : records) {
                //　正常这里应该使用线程池处理，不应该在这里处理
                System.out.printf("offset = %d, key = %s, value = %s", record.offset(), record.key(), record.value() + "\n");
                if (record.value().contains("A")) {
                    deal = false;
                }
            }
            if(deal == false){
                break;
            }
        }
        consumer.close();
        System.out.println("Char 'A' received, exit!");
    }
}
