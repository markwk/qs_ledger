# Apple Health Data Extractor, Data Analysis, and Elastic Search Integration and Dashboard

This project can help you convert your Apple Health data into something useful and usable! The code has been broken down into separate scripts to handle the process step-by-step. 

For more information and a walkthrough of some of the key steps in the process see [How to Export, Parse and Explore Your Apple Health Data With Python](http://www.markwk.com/data-analysis-for-apple-health.html). 

### Extracting and Processing Your Apple Health XML into CSVs and some simple data analysis

- Step 1: Export Apple Health data from the Health on iOS
- Step 2: Download to your computer and decompress the file and place in the apple_health directory instead of qs_ledger. It should look something like your-path-here/qs_ledger/apple_health_export/export.xml
- Step 3: Open up and run the jupyter notebook **apple_health_extractor.ipynb**. This script will parse your XML file and convert it into a series of CSV files. It essentially walks you through a process that runs the python script apple-health-data-parser.py which you can alternatively run directly in terminal or command line. 
- Step 4 (optional):  Open up and run the jupyter notebook **apple_health_data_processor.ipynb** for some additional data processing and simple data analysis using pandas and matplotlib. 

### Integrating with Elastic Search and Creating a Kibana Apple Health Dashboard

This part is entirely optional but it will enable you to view and explore your data inside of Elastic Search. This part assumes you have downloaded and setup Elastic Search either locally or in the cloud. 

- Step 1 (if running locally): Start Elastic with `bin/elasticsearch`
- Step 2: Install Espandas using the following command: `python -m pip install https://github.com/markwk/espandas/archive/master.zip` (Note: At the time of this project, the main project has a bug so you'll need to either download this fork or make some manual changes to the original code. [See issue here](https://github.com/dashaub/espandas/issues/2).)
- Step 3: Open up and run the jupyter notebook **apple_health_data2elastic.ipynb** in order to modify your data into Elastic Search compatible format and then import it into Elastic Indexes. (NOTE: The script currently uses a workaround with the file `apple_health_elastic_mapping.json` to mapping your fields into Elastic compatible format. You can check the mappings by running the following command `curl -X GET "localhost:9200/steps/_mapping?pretty"`)
- Step 4: Run the following command to confirm data imported correctly 

```
curl -H "Content-Type: application/json" -XGET localhost:9200/steps/_count -d '{
        "query": {
                "match_all": {}
        }
}'
```

- Step 5 (if running locally): Start Kibana `bin/kibana` and navigate to it locally at http://localhost:5601. 
- Step 6: In Kibana use the sidebar menu to navigate to Management > Stack Management and finally choose the option **Index Patterns** under "Kibana."
- Step 7: Select the button for "Create index pattern" and then type in the name of one of your indexes like `steps` and hit "Next Step."
- Step 8: Then use the time field option and select `date` and hit "Create index pattern."
- Repeat 6-8 to create additional index patterns for hr and resting_hr.  
- Step 9: Navigate to the menu item **Saved Objects** under Kibana.
- Step 10: Select option for **Import** and either drag and drop or select the file `apple_health_elastic_dashboard.ndjson` which will create a few sample charts and an Apple Health Dashboard which you can view in Kibana and looks something like this: 

![](https://raw.githubusercontent.com/markwk/qs_ledger/master/apple_health/apple_health_elastic_dashboard_example.png)

Best of luck extract, parsing and visualizing your apple health data! 