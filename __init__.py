"""
Some commonnly used functions / strings
in deployment scenarios.
"""

PKG_SETUP_CMD = \
    """
    PKG_OK=$(dpkg-query -W --showformat='${{Status}}\n' {0} |
        grep "install ok installed");
        if [ "" == "$PKG_OK" ]; then
            echo "No {0}. Setting up {0}."
            apt-get -y update;
            apt-get --force-yes --yes install {0}
        fi
    """

ADD_USER_CMD = \
    """
    id -u {0} &>/dev/null || useradd {0}
    """


ADD_GROUP_CMD = \
    """
    getent group {0} &>/dev/null || groupadd {0}
    """
