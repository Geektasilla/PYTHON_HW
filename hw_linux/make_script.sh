	#!/bin/bash
read -p "Enter path for script: " SCRIPT_PATH
read -p "Enter name for your script: " NAME
mkdir -p $SCRIPT_PATH

ls $SCRIPT_PATH/$NAME 2>/dev/null
if [ $? -eq 0 ]
   then
    echo "BAD NAME $SCRIPT_PATH/$NAME"
   else
    echo "#!/bin/bash" > $SCRIPT_PATH/$NAME 
    echo "#" >> $SCRIPT_PATH/$NAME
    echo "#Write the code here" >> $SCRIPT_PATH/$NAME
    chmod +x $SCRIPT_PATH/$NAME
    nano $SCRIPT_PATH/$NAME
fi
echo "done"
 
