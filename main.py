#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Fonctions d'affichage d'une donnée sur une carte.
"""

### import *all packages*
# Ecriture de la fonction 

# Il n'y a plus qu'à tout rentrer dans la grosse fonction 
def plot_geo_time_value(x, y, years, df, hue, proj,axs):
    """
    Visualise l'évolution temporelle d'une donnée numérique
    géolocalisée.

    :param x: longitudes (vecteur)
    :param y: latitudes (vecteur)
    :param year: années (vecteur)
    :param value: valeurs numériques à représenter (DataFrame ou numpy array de taille n_observations * n_years)
    :param proj: méthode de projection (mercator ou platecarree) (string)
    :param axs: axes matplotlib sur lesquels tracer (vecteur ou numpay array)
    :param name: noms des lieux  (vecteur)
    :param hue: sens de la valeur numérique (:math:`CO_2`, Ammoniac, ...)
    :param kwargs: paramètres additionnels
    """
    if proj=="Mercator":
        ### Transformation des coordonnées
        p1 = Proj(init='epsg:3395')  # projection Mercator


        p2 = Proj(init='epsg:27572')  # Lambert II étendu: format initial, ne pas toucher 


        # Transformation des coordonnées de localisation pour la projection utilisée 
        long, lat = transform(p2, p1, x, y) 

        # Ajout de deux colonnes contenant les coordonnées de localisation adaptées à la projection utilisée
        df2['LLX'] = long
        df2['LLY'] = lat
        
        ### Tracé des cartes qui nous intéressent 
        for i in years:

            ## Options de présentation 
            fig = plt.figure(figsize=(15,15)) 
            ax = fig.add_subplot(1, 1, 1, projection=ccrs.Mercator())

            ax.set_extent(axs)

            ax.add_feature(cfeature.OCEAN.with_scale('50m'))
            ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
            ax.add_feature(cfeature.RIVERS.with_scale('50m'))
            ax.add_feature(cfeature.LAKES.with_scale('50m'))
            ax.add_feature(cfeature.BORDERS.with_scale('50m'), linestyle=':')

            ax.set_title(hue+" en France en "+str(i));

            ## Placement des points d'intérêt 
            ax.scatter(long, lat, s=df[[hue+"_"+str(i)]].apply(pd.to_numeric) ** 0.5 / 15, alpha=0.5)

            # Exportation des images 
            plt.savefig('./data/carte'+str(i))
            
    if proj=="PlateCarree":
        ### Transformation des coordonnées 
        ### Paramètres de projection (format des coordonnées de localisation)
        p1 = Proj(init='epsg:4326')  # projection long/lat


        p2 = Proj(init='epsg:27572')  # Lambert II étendu: format initial, ne pas toucher 

        # Transformation des coordonnées de localisation pour la projection utilisée 
        long, lat = transform(p2, p1, x, y) 

        # Ajout de deux colonnes contenant les coordonnées de localisation adaptées à la projection utilisée
        df2['LLX'] = long
        df2['LLY'] = lat
        
        
        ### Tracé des cartes qui nous intéressent 
        for i in years:

            ## Options de présentation 
            fig = plt.figure(figsize=(15,15)) 
            ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

            ax.set_extent(axs)

            ax.add_feature(cfeature.OCEAN.with_scale('50m'))
            ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
            ax.add_feature(cfeature.RIVERS.with_scale('50m'))
            ax.add_feature(cfeature.LAKES.with_scale('50m'))
            ax.add_feature(cfeature.BORDERS.with_scale('50m'), linestyle=':')

            ax.set_title(hue+" en France en "+str(i));

            ## Placement des points d'intérêt 
            ax.scatter(long, lat, s=df[[hue+"_"+str(i)]].apply(pd.to_numeric) ** 0.5 / 15, alpha=0.5)

            # Exportation des images 
            plt.savefig('./data/carte'+str(i))


    image = []
    for i in years:
        image.append(imageio.imread('./data/carte'+str(i)+'.png'))
    output = './data/CarteAnimee.gif'
    imageio.mimsave(output, image, duration = 2)

