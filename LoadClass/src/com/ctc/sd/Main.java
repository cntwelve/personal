package com.ctc.sd;

import java.io.File;
import java.lang.reflect.Method;
import java.net.URL;
import java.net.URLClassLoader;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws Exception {
        String rl = "";
//        Console cons = System.console();
        Scanner input = new Scanner(System.in);

        // wait for key
        System.out.println("If ready, then press any key and return!");
        input.nextLine();

        System.out.println("Start to load class:");
        Class<?> tc = null;
        try {
            tc = Class.forName("com.ctc.jars.test1");
            System.out.println("Loaded from class path!");
        } catch (ClassNotFoundException e) {
            System.out.println("Try to load from file system!");
            Method method_u = URLClassLoader.class.getDeclaredMethod("addURL", URL.class);
            boolean accessible = method_u.isAccessible();
            try {
                if (accessible == false) {
                    method_u.setAccessible(true);
                }
                // 设置类加载器
                URLClassLoader classLoader = (URLClassLoader) ClassLoader.getSystemClassLoader();
                // 从.clas文件中加载
//                method_u.invoke(classLoader, (new File(".")).toURI().toURL());
                // 从jar文件中加载
                method_u.invoke(classLoader, (new File("jars.jar")).toURI().toURL());
            } finally {
                method_u.setAccessible(accessible);
            }
            tc = Class.forName("com.ctc.jars.test1");
            System.out.println("Loaded from file system!");
        }
        System.out.println(tc.getName());

        Object tci = tc.newInstance();
        Method method = tc.getMethod("jartest");
//        method.invoke(tci);

        System.out.println("Please input: ");
        while (true) {
            rl = input.nextLine();
            if (rl.equals("quit")) {
                break;
            } else {
                System.out.println("Readed: " + rl);
                System.out.println(method.invoke(tci));
            }
        }
    }
}
