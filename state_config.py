"""
State configuration for this NorthDakotaDischargeWatch instance.

All state-specific values are centralized here. To deploy for a new state,
run: python deploy_new_state.py <STATE_CODE>

This file is overwritten by deploy_new_state.py — do not add logic here.
"""

STATE_CODE = "ND"
STATE_NAME = "North Dakota"
APP_NAME = "NorthDakotaDischargeWatch"
APP_TAGLINE = "North Dakota Discharge Monitoring"
DOMAIN = "northdakotadischargewatch.org"
DATA_FILE = "nd_exceedances_launch_ready.csv"
CONTACT_EMAIL = "data@northdakotadischargewatch.org"
MAILING_ADDRESS = ""
TIMEZONE_LABEL = "CST"
EPA_REGION = 8
