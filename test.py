from alayout import *

with LinearLayout(width=FILL, height=FILL, orientation=VERTICAL):
	with TextView(id='text', width=WRAP, height=WRAP) as tv:
		tv['text'] = 'Hello, I am a TextView'
	Button(
			id='button', width=WRAP, height=WRAP,
			text='Hello, I am a Button'
		)

"""
Original example XML from the documentation:

<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
              android:layout_width="fill_parent" 
              android:layout_height="fill_parent" 
              android:orientation="vertical" >
    <TextView android:id="@+id/text"
              android:layout_width="wrap_content"
              android:layout_height="wrap_content"
              android:text="Hello, I am a TextView" />
    <Button android:id="@+id/button"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Hello, I am a Button" />
</LinearLayout>
"""
