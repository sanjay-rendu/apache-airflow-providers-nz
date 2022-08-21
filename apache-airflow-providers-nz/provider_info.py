def get_provider_info():
    return {
        "package-name": "apache-airflow-providers-nz",
        "name": "netezza",
        "description": "Airflow Hook for Netezza",
        "hook-class-names": [
            "apache-airflow-providers-nz.hooks.netezza.NetezzaHook",
        ],
    }
