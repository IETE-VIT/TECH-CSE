package com.garv.tandon.parsestartergarv;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.graphics.Paint;
import android.os.Bundle;
import android.util.Log;
import android.view.KeyEvent;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.parse.LogInCallback;
import com.parse.ParseAnalytics;
import com.parse.ParseException;
import com.parse.ParseUser;
import com.parse.SignUpCallback;

public class MainActivity extends AppCompatActivity implements View.OnKeyListener{
    Boolean signupMode = true;
    TextView username;
    TextView password;
    Button signupOrLoginButton, changeMode;

    @Override
    public boolean onKey(View view, int i, KeyEvent keyEvent) {
        if(view.getId() == R.id.Password_textView){
            if(i == KeyEvent.KEYCODE_ENTER && keyEvent.getAction() == KeyEvent.ACTION_DOWN){
                signupOrLogin(view);
            }
        }
        return false;
    }

    public void goToUserListActivity(){
        Intent intent = new Intent(this, UserListActivity.class);
        startActivity(intent);
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        username = findViewById(R.id.Username_textView);
        password = findViewById(R.id.Password_textView);
        signupOrLoginButton = findViewById(R.id.signup_login_button);
        changeMode = findViewById(R.id.changeMode);
        changeMode.setPaintFlags(changeMode.getPaintFlags() | Paint.UNDERLINE_TEXT_FLAG);
        password.setOnKeyListener(this);

        if(ParseUser.getCurrentUser() != null){
            goToUserListActivity();
        }
        ParseAnalytics.trackAppOpenedInBackground(getIntent());
    }
    boolean checkEmpty(){
        if(username.getText().toString().isEmpty() || password.getText().toString().isEmpty()) {
            Toast.makeText(this, "Please enter a username and password", Toast.LENGTH_SHORT).show();
            Log.i("ERROR","EMPTY");
            return true;
        }else{
            return false;
        }
    }
    public void changeMode(View view){
        if(signupMode == true){
            signupOrLoginButton.setText("Login");
            signupMode = false;
            changeMode.setText("or, Sign Up");
        }
        else{
            signupOrLoginButton.setText("Sign Up");
            signupMode = true;
            changeMode.setText("or, Login");
        }
    }
    public void signupOrLogin(View view){
        if(signupMode==true){
        if(checkEmpty()){

        }
        else{
            ParseUser user = new ParseUser();
            user.setUsername(username.getText().toString());
            user.setPassword(password.getText().toString());
            user.signUpInBackground(new SignUpCallback() {
                @Override
                public void done(ParseException e) {
                    if(e == null){
                        Toast.makeText(MainActivity.this, "Signup Successfull", Toast.LENGTH_SHORT).show();
                        goToUserListActivity();
                    }
                    else{
                        Toast.makeText(MainActivity.this, e.getMessage(), Toast.LENGTH_SHORT).show();
                    }
                }
            });
        }}
        else{
            if(checkEmpty()) {

            }else{
                ParseUser.logInInBackground(username.getText().toString(), password.getText().toString(), new LogInCallback() {
                    @Override
                    public void done(ParseUser user, ParseException e) {
                        if(e == null && user != null){
                            Toast.makeText(getApplicationContext(), user.getUsername()+" Signed in", Toast.LENGTH_SHORT).show();
                            goToUserListActivity();
                        }else{
                            Toast.makeText(MainActivity.this, e.getMessage(), Toast.LENGTH_SHORT).show();
                        }
                    }
                });
            }
        }
        }
    }
