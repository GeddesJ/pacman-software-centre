1. Come up with a name

2. Work on GUI - I actually have no idea how pyqt works... should be fun!

3. Need to consider how I can implement the Roll back feature - Do I want a 
button for rolling back entire updates or is that a bad idea? Also I don't 
think that this is implemented in the pyalpm library. 

4. How will packages be organized? I have a sneaking suspicion that pacman 
doesn't store as much metadata as apt or rpm, so it will be difficult to break 
every package into categories using some automatic system using the package 
metadata. At the moment I am thinking that I will have a general search to 
search for any package, and then I will have a section where the most popular 
linux apps are broken into categories. This will definitely have to be what I 
will have to do for the AUR aspect, ain't nobody got time to index the entire 
AUR. 

5. There needs to be a system tray icon and a process for checking for updates 
in the background. Could be getting into SystemD territory.

6. I would like to use icons from the user's system icons to provide pictures 
for the packages, so not only will the package manager integrate well with the 
user's themes but it will look more appealing. Problem is, I will definitely 
need a fallback if there are missing icons.
