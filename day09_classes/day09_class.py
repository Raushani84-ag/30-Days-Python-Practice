class EnergyRecord:  # Define the class skeleton
    """
    Represents a single energy sensor reading.
    """
    def __init__(self, site_id, timestamp, demand_kw):
        self.site_id = site_id
        self.timestamp = timestamp
        self.demand_kw = demand_kw

    # Adding a Validation Method
    def is_valid(self):
        """
        Validate the energy record.
        Returns (True , None) if valid, else (False, reason).

        """
        if not isinstance(self.site_id, str) or not self.site_id:
            return False, "Invalid or missing site_id"

        if not isinstance(self.demand_kw, (int, float)):
            return False , "demand must be numeric"

        if self.demand_kw < 0:
            return False , "demand must be non-negative"

        return True, None

#     Adding a Normalization Method
    def normalize(self):
        '''
        Normalize the energy record in-place
        '''
        self.site_id = self.site_id.strip().upper()
        self.demand_kw = float(self.demand_kw)

    #Adding export method
    def to_dict(self):
        """
        Convert the record to a dictionary
        """
        return  {
            "site_id" : self.site_id,
            "timestamp": self.timestamp,
            "demand_kw": self.demand_kw
        }

if  __name__ =="__main__":
    record = EnergyRecord(" s1 ", "2024-01-01 08:00", 120)

    print(record.is_valid())
    record.normalize()
    print(record.to_dict())
