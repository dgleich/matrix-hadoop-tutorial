
TARGETS=getdata 

all:
	@echo ""
	@echo "Please run make for one of the following targets:"
	$(foreach tar,$(TARGETS),@echo "  make $(tar)";)
	@echo ""

data:
	mkdir data
	
data/user_ratings.txt.gz:
	wget -O data/user_ratings.txt.gz http://www.trustlet.org/datasets/extended_epinions/user_rating.txt.gz

data/mc.txt.gz:
	wget -O data/mc.txt.gz http://www.trustlet.org/datasets/extended_epinions/mc.txt.gz
	
data/rating.txt.gz:
	wget -O data/rating.txt.gz http://www.trustlet.org/datasets/extended_epinions/rating.txt.gz

	
datafiles: data	data/user_ratings.txt.gz data/mc.txt.gz data/rating.txt.gz
	
	
getdata: datafiles
	

.PHONY: all $(TARGETS) datafiles
