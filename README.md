# astro
simple script to stay in touch with the space

## Installation
* Change the path in the ExecStart declaration of the astro.service file.
* Change the OnCalendar section in the astro.timer file appropriately.
* Copy both files to ~/.config/systemd/user/
* Run following commands:
 systemctl --user daemon-reload
 systemctl --user start astro.timer
