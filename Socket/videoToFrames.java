import java.io.*;

class videoToFrames{
    public static void main(String args[]){
    try{
        Process process = Runtime.getRuntime().exec("ffmpeg -i video.mp4 -r 4 snapshots/outputFile_%02d.png");
    }catch(IOException ex){}
    
    }

}
