## 📟 Systemd

Creating **echotcp** systemd configuration file

```bash
nano /etc/systemd/system/echotcp.service
```

```ini
[Unit]
Description=Echo TCP/IP application

[Service]
Environment="PYTHONPATH=/root/pylib"
ExecStart=/root/echotcp/venv/bin/python server.py
WorkingDirectory=/root/echotcp
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

Run **echotcp** service

```bash
systemctl daemon-reload # reload
systemctl start echotcp.service # enable now
systemctl enable echotcp.service # enable with power-up
systemctl status echotcp.service # check status
```