# Scraped-Products-Info-for-Project-Rest_API-with-Flask
These products details were scraped for affiliate website project. They will stored in database that can be retrieved from Rest APIs (in different project). The original website maybe Amazon or AliExpress
## Project Objectives:
- Gather products data
- Clean data
- Store data
## Method Used:
- Data scraping
- Data Cleaning
- Data Entry
## Tools Used:
- Python
## Libraries:
- BeautifulSoup
- Selenium
## Step-by-step:
### Determine the type of data need to be scraped
- Name of products
- Image links
- Product links
- Product descriptions
- Prices
- Stars Rate
### Examinie the structure of source website HTML, explore the containers and sections contain these data
- Inspect website sources
- Use proper accessible methods to find the needed sections that data is located
### Write codes executing these features to achieve the goals
```python
soup = BeautifulSoup(driver.page_source, 'lxml')
product_card = soup.find_all('div', {"class":'ng-scope',"ng-if":"::post.type == 'post'"})
df=pd.DataFrame({'Product_name':[''], 'Product_link':[''], 'Product_price':[''], 'Product_description':[''], 'Product_image':[''], 'Product_sales':['']})
for product in product_card:
    try:
        product_name = product.find('a', class_='ng-binding ng-scope').text
        product_link = product.find('a', class_='ng-binding ng-scope').get('href')
        product_price = product.find('div', class_='price ng-binding').text
        product_description = product.find('p', class_='ng-binding').text
        product_image = product.find('img', class_='img-fixed lazy-image--handled').get('src')
        product_sales = product.find('a', class_='saved-count ng-binding').text
        df= df.append({'Product_name':product_name, 'Product_link':product_link, 'Product_price':product_price, 'Product_description':product_description,'Product_image':product_image,'Product_sales':product_sales }, ignore_index=True)
    except:
        pass
df
```
#### Products information result
![image](https://github.com/KeithDang1610/Scraped-Products_details-for-Project-Rest_API-with-Flask/assets/167521177/bfce2e97-5069-4ce0-aa23-1054cb99995f)

### Clean data
The scraped data will undergo processing and cleaning to ensure accurate results before being stored in the database.
