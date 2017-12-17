import java.io.*;
import java.io.File;

class vidToFrames{
    public static void main(String args[]){
   // Process p = new ProcessBuilder("ffmpeg -i video.mp4 -r 4 snapshots/outputFile_%02d.png
   //", "").start();
   
   final String dir_string = System.getProperty("user.dir")+"/snapshots/";
   File dir = new File(dir_string);

    System.out.println(dir);
    
    if(!dir.exists())dir.mkdir();


    for(File file: dir.listFiles()) 
        if (!file.isDirectory()) 
        file.delete();
        
   try{
        Process process = Runtime.getRuntime().exec("ffmpeg -i "+ args[0] + " -r 0.5 snapshots/outputFile_%02d.png");
     }catch(IOException ex){}
    
    }


}
