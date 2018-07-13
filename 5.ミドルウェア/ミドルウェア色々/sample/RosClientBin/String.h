#pragma once
#include "stdafx.h"
#using "RosClientBin/RosClient.dll"
#include <string>
#include "msclr/marshal.h"
#include "msclr/marshal_windows.h"
#include "msclr/marshal_cppstd.h"
#include "msclr/marshal_atl.h"

using namespace System::Collections::Generic;
using namespace RosSharp;


static System::String^ ToStr( const char* str )
{
	return gcnew System::String( str );
}

static System::String^ ToStr( CString str )
{
	return gcnew System::String( str );
}

static System::String^ ToStr( List<byte> ^str )
{
	return RosClient::ToString( str );
}

static char* ToChar( System::String ^str )
{
	static char cstr[1024];
	strcpy( cstr , msclr::interop::marshal_as<std::string>(str).c_str() );
	return cstr;
}

static char* ToChar( List<byte> ^str )
{
	return ToChar( ToStr(str) );
}

static List<byte>^ ToBytes( System::String ^str )
{
	return RosClient::ToBytes( str );
}

static List<byte>^ ToBytes( const char *str )
{
	return RosClient::ToBytes( gcnew System::String(str) );
}

static List<byte>^ ToBytes( CString str )
{
	return RosClient::ToBytes( gcnew System::String(str) );
}
