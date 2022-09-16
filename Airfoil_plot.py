#imports
import requests
import matplotlib.pyplot as plt

while True:
    def get_airfoil_coords(airfoil:str):
        url = 'https://m-selig.ae.illinois.edu/ads/coord/{}.dat'.format(airfoil.lower())
        response_text = requests.get(url).text
        if 'Not Found' in response_text:
            raise NameError('{} not found in UIUC database'.format(airfoil))
        all_text = response_text.split('\n')
        x_coords, y_coords = [],[]
        plot_title = ''
        
        for index, line in enumerate(all_text):
            if index == 0:
                plot_title = line.strip()
            else:
                try:
                    line = line.strip()
                    x,y = line.split(' '*line.count(' '))
                    x = float(x.strip())
                    y = float(y.strip())
                    if x <= 1.0 and y <= 1.0: 
                        x_coords.append(x)
                        y_coords.append(y)
                except ValueError:
                    continue
        return x_coords,y_coords,plot_title
        
    def plot_airfoil(x_coords:list, y_coords:list, plot_title:str):
        plt.plot(x_coords,y_coords,'k-')
        plt.title('{} airfoil'.format(plot_title))
        plt.style.use('default')
        plt.xlim(-0.50,1.25)
        plt.ylim(-1,1)
        plt.show()
    
    air_foil = input("Enter the airfoil name without space in lowerCase: ")
    try:
        x_values, y_values, title = get_airfoil_coords(air_foil)
        plot_airfoil(x_values, y_values, title)
    except NameError:
        print('{} not in UIUC database, try again!'.format(air_foil)) 

