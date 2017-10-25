package com.randomware.signlanguageinterpreter;

import android.content.Context;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.Socket;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    Context context;
    EditText getIP;

    private boolean isConnected = false;
    private Socket socket;
    private PrintWriter out;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        context = this; //save the context to show Toast messages

        //reference to edittext
        getIP = (EditText) findViewById(R.id.getIP);



    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_connect) {
            ConnectPhoneTask connectPhoneTask = new ConnectPhoneTask();
            connectPhoneTask.execute(getIP.getText().toString()); //try to connect to server in another thread
            return true;
        }

        return super.onOptionsItemSelected(item);
    }



    @Override
    protected void onStop() {
        super.onStop();
    }

    //OnClick method is called when any of the buttons are pressed
    @Override
    public void onClick(View v) {


    }

    @Override
    public void onDestroy() {
        super.onDestroy();
        if (isConnected && out != null) {
            try {
                out.println("exit"); //tell server to exit
                socket.close(); //close socket
            } catch (IOException e) {
                Log.e("remotedroid", "Error in closing socket", e);
            }
        }
    }

    public class ConnectPhoneTask extends AsyncTask<String, Void, Boolean> {

        @Override
        protected Boolean doInBackground(String... params) {
            boolean result = true;
            try {
                InetAddress serverAddr = InetAddress.getByName(params[0]);
                socket = new Socket(serverAddr, Constants.SERVER_PORT);//Open socket on server IP and port
            } catch (IOException e) {
                Log.e("remotedroid", "Error while connecting", e);
                result = false;
            }
            return result;
        }

        @Override
        protected void onPostExecute(Boolean result) {
            isConnected = result;
            Toast.makeText(context, isConnected ? "Connected to server!" : "Error while connecting", Toast.LENGTH_LONG).show();
            try {
                if (isConnected) {
                    out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(socket
                            .getOutputStream())), true); //create output stream to send data to server

                }
            } catch (IOException e) {
                Log.e("remotedroid", "Error while creating OutWriter", e);
                Toast.makeText(context, "Error while connecting", Toast.LENGTH_LONG).show();
            }
        }
    }
}