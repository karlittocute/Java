/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication1;

import java.io.*;
import java.util.*;

public class JavaApplication1 
{

 
    public static String get_a_key() //получение ключа
    {
         System.out.print("Enter a key: ");
         Scanner sc = new Scanner(System.in); //создаём объект sc класса Scanner
         String key = "";    //объявляем. Переменные НУЖНО обнулять.
         key = sc.nextLine(); //считываем, присваеваем
         return key;  //возвращаем
    }
    
    public static void encode() //кодировать. Кодируем всегда из файла 1 в файл 2.
    {
        
        String key = get_a_key(); //получаем ключ кодирования
        String message = ""; //обнуляем послание
        
        try(FileReader reader = new FileReader("1.txt")) //пытаемся найти файл 1 и создать на его основе reader типа FileReader
        {
            int c;  //тут сложно. мы считываем числом
            while((c=reader.read())!=-1) //если оно существует
            {
                message += ((char)c); //а потом добавляем соответсвенную чарку к посланию. Так нужно, просто поверь. 
            }   //Чистая магия. Без неё не работает.
        }
        catch(IOException ex)   //если файла нет, выкидываем исключение, программа закончится. Что поделать. Зато без глобальных переменных.
        {
            System.out.println("Error 2: file with message is not found!");
        }
        
        
        byte[] txt = message.getBytes(); //преобразуем послание в массив байтов
	byte[] k = key.getBytes();  //и ключ
	byte[] res = new byte[message.length()]; //это будущее закодированное сообщение.

		for (int i = 0; i < txt.length; i++) 
                {
			res[i] = (byte) (txt[i] ^ k[i % k.length]); //Ксорим i-ый байт сообщения и i-ый байт ключа и заносим результат в res
		}
                
	String result = new String(res); // такие дела. Я не виноват. Типа нам надо стринг получить, а мне лень проверять, будет ли работать иначе.
                                            //(скорее всего, будет)
        
         try(FileWriter writer = new FileWriter("2.txt", false)) //пытаемся найти файл 2 и создать на его основе writer типа FileWriter
        {
            writer.write(result); //записываем результат в файл.
            writer.flush(); //очищаем поток записи.
        }
        catch(IOException ex)// если файла нет, выкидываем исключение.
        {
            System.out.println("Error 3: there is no file to save encoded message!");
        } 
         
    }
    
    public static void decode() // Тут всё точь-в-точь как в encode(), но меняем файлы местами, так как (a XOR b) XOR b = a.
    {
	String key = get_a_key();
        String message = "";
        
        try(FileReader reader = new FileReader("2.txt"))
        {
            int c;
            while((c=reader.read())!=-1)
            { 
                message += ((char)c);
            }
        }
        catch(IOException ex)
        {
            System.out.println("Error 4: file with encoded message is not found!");
        }
        
        
        byte[] txt = message.getBytes();
	byte[] k = key.getBytes();
	byte[] res = new byte[message.length()];
        
	for (int i = 0; i < txt.length; i++) 
        {
            res[i] = (byte) (txt[i] ^ k[i % k.length]);
	}
                
	String result = new String(res);
        
        try(FileWriter writer = new FileWriter("1.txt", false))
        {
            writer.write(result);
            writer.flush();
        }
        catch(IOException ex)
        {
            System.out.println("Error 5: there is no file to save decoded message!");
        } 	
    }
    
    public static void main(String[] args) 
    {
        System.out.println("Choose an option:");
        System.out.println("1. Encode text;");
        System.out.println("2. Decode text;");
        Scanner sc = new Scanner(System.in);    //создаём объект sc класса Scanner
        boolean b = false;  //эта булка нам нужна дальше для защиты от дураков
        String s = ""; // Всегда нужно обнулять переменные
        while (!b)  //защита от дураков, чтоб ввели 1 или 2
        {
            s = sc.nextLine(); //считываем входной поток и записываем в s.
            switch (s) //дальше смотрим на s
            {
                case "1": //если 1
                    encode();   //то кодируем
                    b = true; //булка становится верной =>
                    break;  // выходим из цикла
                case "2":   //есди 2
                    decode();   //то декодируем
                    b = true;   //булка становится верной =>
                    break;  // выходим из цикла
                default:    // любой другой вариант
                    System.out.println("Error 1: you have to type '1' or '2'!");
                    break; //возвращаемся в начало цикла
            } 
        }
        
    }
}
    
