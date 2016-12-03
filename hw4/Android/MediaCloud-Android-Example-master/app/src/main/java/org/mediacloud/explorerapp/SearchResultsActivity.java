package org.mediacloud.explorerapp;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.design.widget.NavigationView;
import android.support.v4.view.GravityCompat;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.LayoutInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.Response;

import org.json.JSONObject;

public class SearchResultsActivity extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener {

    private String inputQuery = null;
    private ImageView mStatusImage;
    public AlertDialog.Builder builder;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_search_results);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawer.setDrawerListener(toggle);
        toggle.syncState();

        Intent intent = getIntent();
        String query = intent.getStringExtra("query");
        mStatusImage = (ImageView) findViewById(R.id.img_view);
        builder = new AlertDialog.Builder(this);
        LayoutInflater inflater = getLayoutInflater();
        View dialogView = inflater.inflate(R.layout.dialog_layout, null);
        builder.setView(dialogView);
        builder.setMessage("Sorry an error occured for this search!")
                .setTitle("Search failed");



        if (query != null) {
            TextView resultsTextView = (TextView) findViewById(R.id.results);
            if(query.equals("about")){
                resultsTextView.setText("This is the about page for explanation to users of this app.");
                mStatusImage.setImageResource(R.mipmap.manual);
            }
            else {
                inputQuery = query;
                resultsTextView.setText("Running query for " + inputQuery + "...");
                new SimpleQuery().execute(inputQuery);
                mStatusImage.setImageResource(R.mipmap.search);
            }
        }
        else{
            mStatusImage.setImageResource(R.drawable.hello);
        }

        NavigationView navigationView = (NavigationView) findViewById(R.id.nav_view);
        navigationView.setNavigationItemSelectedListener(this);
    }

    private class SimpleQuery extends AsyncTask<String, Void, Integer> {
        protected Integer doInBackground(String... queryTexts) {
            OkHttpClient client = new OkHttpClient();
            String queryText = queryTexts[0];
            String path = "sentences/count?q="+queryText+"&fq=media_sets_id:1&key="+MediaCloudClient.API_KEY;
            String url = "https://api.mediacloud.org/api/v2/"+path;
            Request request = new Request.Builder()
                    .url(url)
                    .build();

            try {
                Response response = client.newCall(request).execute();
                String jsonData = response.body().string();
                JSONObject jsonObject = new JSONObject(jsonData);
                return jsonObject.getInt("count");
            } catch (Exception e){
                return -1;
            }
        }
        protected void onPostExecute(Integer result) {
            String contentToShow = "Error :-(";
            if (result != -1){
                contentToShow = "Found "+result+" sentences mentioning "+inputQuery;
            }
            else{
                AlertDialog dialog = builder.create();
                dialog.show();
            }

            TextView resultsTextView = (TextView) findViewById(R.id.results);
            resultsTextView.setText(contentToShow);
        }
    }

    @Override
    public void onBackPressed() {
        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        if (drawer.isDrawerOpen(GravityCompat.START)) {
            drawer.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }

    @SuppressWarnings("StatementWithEmptyBody")
    @Override
    public boolean onNavigationItemSelected(MenuItem item) {
        // Handle navigation view item clicks here.
        int id = item.getItemId();

        if (id == R.id.nav_search_kittens) {
            Intent i = new Intent(this, SearchResultsActivity.class);
            i.putExtra("query", "kittens");
            startActivity(i);
        } else if (id == R.id.nav_search_puppies) {
            Intent i = new Intent(this, SearchResultsActivity.class);
            i.putExtra("query", "puppies");
            startActivity(i);
        } else if (id == R.id.nav_search_robots) {
            Intent i = new Intent(this, SearchResultsActivity.class);
            i.putExtra("query", "robots");
            startActivity(i);
        }else if (id == R.id.nav_about_activity) {
            Intent i = new Intent(this, SearchResultsActivity.class);
            i.putExtra("query", "about");
            startActivity(i);
        }

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        drawer.closeDrawer(GravityCompat.START);
        return true;
    }
}
